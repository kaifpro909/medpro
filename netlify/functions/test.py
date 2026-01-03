"""
Simple test function to verify Netlify Functions are working
"""
import json

def handler(event, context):
    """
    Simple test handler to verify Netlify Functions work
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            'message': 'Netlify Function is working!',
            'path': event.get('path', 'unknown'),
            'method': event.get('httpMethod', 'unknown')
        })
    }

