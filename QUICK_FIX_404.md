# Quick Fix for 404 Error on Netlify

## Immediate Steps to Fix 404

### Step 1: Verify Function Exists
1. Go to Netlify Dashboard → Your Site → **Functions** tab
2. Check if `server` function is listed
3. If missing, the function didn't deploy - check build logs

### Step 2: Test Function Directly
Try these URLs (replace with your site URL):
- `https://your-site.netlify.app/.netlify/functions/test` - Should return JSON
- `https://your-site.netlify.app/.netlify/functions/server` - Should return Flask app

### Step 3: Check Build Logs
1. Netlify Dashboard → **Deploys** → Latest deploy
2. Look for:
   - ✅ "Functions bundled successfully"
   - ❌ Any Python/import errors
   - ❌ Missing file errors

### Step 4: Verify Files Are Committed
Ensure these files are in your git repository:
```bash
git status
# Should show:
# - netlify/functions/server.py
# - netlify.toml
# - requirements.txt
```

### Step 5: Rebuild with Cache Clear
1. Netlify Dashboard → Deploys
2. Click **"Trigger deploy"** → **"Clear cache and deploy site"**

## Common Causes

### Cause 1: Function Not Deploying
**Fix**: Check that `netlify/functions/server.py` exists and is committed

### Cause 2: Import Errors
**Fix**: Check build logs for missing dependencies or import errors

### Cause 3: Wrong Function Path
**Fix**: Verify redirect in `netlify.toml` points to `/.netlify/functions/server`

### Cause 4: Python Runtime Issues
**Fix**: Ensure `PYTHON_VERSION = "3.11"` in `netlify.toml`

## Quick Test

Run this in your terminal to test locally:
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Test locally
netlify dev
```

Then visit `http://localhost:8888` - if it works locally but not on Netlify, it's a deployment issue.

## Still Getting 404?

1. Check function logs: Netlify Dashboard → Functions → server → Logs
2. Look for error messages
3. Share the error with support or check `TROUBLESHOOTING.md` for detailed help

