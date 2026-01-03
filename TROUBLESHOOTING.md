# Troubleshooting Netlify Deployment

## 404 Error - Page Not Found

If you're seeing a 404 error, follow these steps:

### 1. Check Function Deployment

1. Go to Netlify Dashboard → Your Site → Functions
2. Verify that `server` function appears in the list
3. Check function logs for errors

### 2. Test the Function Directly

Try accessing the function directly:
- `https://your-site.netlify.app/.netlify/functions/server`
- `https://your-site.netlify.app/.netlify/functions/test`

If the test function works but server doesn't, there's an issue with the Flask app setup.

### 3. Check Build Logs

1. Go to Netlify Dashboard → Deploys
2. Click on the latest deploy
3. Check for:
   - Python installation errors
   - Missing dependencies
   - Import errors
   - Path resolution issues

### 4. Common Issues

#### Issue: Function not found
**Solution**: 
- Verify `netlify/functions/server.py` exists
- Check `netlify.toml` has `directory = "netlify/functions"`
- Ensure file is committed to git

#### Issue: Import errors
**Solution**:
- Verify all dependencies in `requirements.txt`
- Check that `serverless-wsgi` is installed
- Ensure `app.py` and all imports are in `included_files`

#### Issue: Path resolution errors
**Solution**:
- The function should handle path resolution automatically
- Check function logs for specific path errors
- Verify `Training.csv` and `Testing.csv` are included

#### Issue: Database errors
**Solution**:
- SQLite in `/tmp` won't persist - this is expected
- For production, use a cloud database
- Set `DATABASE_URL` environment variable

### 5. Debug Steps

1. **Check function logs**:
   ```bash
   # In Netlify Dashboard → Functions → server → Logs
   ```

2. **Test locally**:
   ```bash
   npm install -g netlify-cli
   netlify dev
   ```
   This will show errors locally before deploying.

3. **Add debug output**:
   The function now includes error tracebacks - check the function logs for detailed errors.

### 6. Verify Configuration

Check `netlify.toml`:
- Build command is correct
- Functions directory is `netlify/functions`
- Redirects are configured correctly
- `included_files` contains all necessary files

### 7. Environment Variables

Ensure these are set in Netlify Dashboard:
- `SECRET_KEY` - Required
- `NETLIFY=true` - Helps with environment detection
- `FLASK_ENV=production` - Optional but recommended

### 8. Alternative: Use Test Function

If the main function doesn't work, test with the simple test function:
- Access: `/.netlify/functions/test`
- If this works, the issue is with Flask app setup
- If this doesn't work, the issue is with Netlify Functions configuration

### 9. Check File Structure

Ensure your repository has:
```
.
├── app.py
├── netlify.toml
├── requirements.txt
├── netlify/
│   └── functions/
│       ├── server.py
│       └── requirements.txt
├── templates/
├── static/
├── Training.csv
└── Testing.csv
```

### 10. Still Not Working?

1. Check Netlify Community Forums
2. Review Netlify Function logs in detail
3. Consider using Netlify's support
4. Try deploying a minimal Flask app first to verify setup

## Quick Fixes

### Rebuild Site
1. Netlify Dashboard → Deploys
2. Click "Trigger deploy" → "Clear cache and deploy site"

### Check Python Version
- Ensure `runtime.txt` specifies Python 3.11
- Or set in `netlify.toml` build environment

### Verify Dependencies
```bash
# Test locally
pip install -r requirements.txt
python -c "from app import app; print('OK')"
```

