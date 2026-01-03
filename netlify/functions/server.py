"""
Netlify serverless function for Flask app
This function handles all Flask routes through Netlify Functions
"""
import sys
import os
import json

# Get the absolute path to the project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))

# Add project root to Python path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set environment variable for Netlify
os.environ['NETLIFY'] = 'true'

# Change to project root directory for relative paths
os.chdir(project_root)

# Import the Flask app
try:
    from app import app, create_tables
    
    # Initialize database on first import (in serverless, this happens per invocation)
    # Note: SQLite in /tmp won't persist between invocations
    try:
        with app.app_context():
            create_tables()
    except Exception as e:
        print(f"Database initialization note: {e}")
except Exception as e:
    print(f"Error importing app: {e}")
    import traceback
    traceback.print_exc()
    app = None

def handler(event, context):
    """
    Netlify serverless function handler
    Uses serverless-wsgi to adapt Flask to Netlify Functions
    """
    if app is None:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Flask app not initialized'})
        }
    
    try:
        from serverless_wsgi import handle_request
        return handle_request(app, event, context)
    except ImportError as e:
        # Fallback if serverless-wsgi is not available
        import traceback
        error_msg = f'serverless-wsgi package is required. Error: {str(e)}\n{traceback.format_exc()}'
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': error_msg
        }
    except Exception as e:
        import traceback
        error_msg = f'Server error: {str(e)}\n{traceback.format_exc()}'
        print(error_msg)
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': error_msg
        }

