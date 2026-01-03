# Netlify Build Error Fix

## Issues Fixed

### 1. Runtime.txt Format
- **Before**: `python-3.11.0` (not recognized by mise)
- **After**: `python-3.11.4` (standard Netlify format)

### 2. Build Command
- Simplified to avoid Python path issues
- Removed `python -m` prefix (pip should be available after runtime setup)

### 3. Environment Variables
- Removed `PYTHON_VERSION` from `build.environment` (conflicts with runtime.txt)
- Kept `NETLIFY=true` for app detection

## Files Changed

1. **runtime.txt**: Updated to `python-3.11.4`
2. **netlify.toml**: Simplified build command and removed PYTHON_VERSION

## If Build Still Fails

### Option 1: Use Default Python
Remove `runtime.txt` entirely and let Netlify use default Python version.

### Option 2: Try Different Runtime Format
Try these formats in `runtime.txt`:
- `3.11.4` (just version number)
- `python-3.11` (major.minor only)

### Option 3: Specify in netlify.toml Only
Remove `runtime.txt` and add back to `netlify.toml`:
```toml
[build.environment]
  PYTHON_VERSION = "3.11"
```

### Option 4: Use .python-version Instead
Create `.python-version` file with:
```
3.11.4
```

## Verification

After committing changes:
1. Push to repository
2. Trigger new deploy on Netlify
3. Check build logs for:
   - ✅ "Installing Python 3.11.4"
   - ✅ "Installing dependencies"
   - ❌ Any mise errors

## Current Configuration

- **Runtime**: `runtime.txt` with `python-3.11.4`
- **Build Command**: `pip install --upgrade pip && pip install -r requirements.txt`
- **Functions**: `netlify/functions` directory

