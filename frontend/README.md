# AcousticSpace - Deepfake Detection Frontend

## Project Fixed ✅

### Problems Solved:

1. **Missing Dependencies** - Created `package.json` with React, React DOM, TypeScript, and Vite
2. **Missing Components** - Created the missing `WaveformPlayer` component
3. **Incorrect File Structure** - Reorganized code into proper `src/` directory with `components/` subfolder
4. **Import Path Issues** - Fixed all import paths to match new structure
5. **Missing Configuration Files** - Created:
   - `tsconfig.json` - TypeScript configuration
   - `tsconfig.node.json` - TypeScript for build tools
   - `vite.config.ts` - Vite bundler configuration
   - `index.html` - HTML entry point
   - `src/main.tsx` - React entry point

### Project Structure:

```
frontend/
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── .gitignore
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── styles.css
│   └── components/
│       ├── AudioUploader.tsx
│       ├── ResultsPanel.tsx
│       └── WaveformPlayer.tsx
```

## Next Steps:

### 1. Install Node.js
If you don't have Node.js installed, download it from https://nodejs.org/ (LTS version recommended)

### 2. Install Dependencies
```bash
cd frontend
npm install
```

### 3. Start Development Server
```bash
npm run dev
```

The app will run on `http://localhost:3000`

### 4. Build for Production
```bash
npm run build
```

## Features:

- 🎙️ Audio file upload
- 📊 Real-time waveform visualization
- 🔍 Deepfake detection analysis
- 📈 Results dashboard with confidence scores
- 🎨 Modern dark UI with gradient styling

## Backend Connection:

The frontend connects to the backend API at `http://localhost:8000/analyze`

Make sure your backend service is running on port 8000 for the analysis feature to work.
