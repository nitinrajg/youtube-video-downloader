# vieUrl - Video Downloader

A modern web application built with Next.js that allows users to download videos from YouTube and Instagram with various quality options.

## Features

- 🎥 Support for both YouTube and Instagram video downloads
- 🎨 Modern, responsive UI with animated gradients
- ⚡ Fast video processing and downloads
- 📊 Multiple quality options for downloads
- 🖼️ Video preview with thumbnail and metadata
- 📱 Mobile-friendly design
- 🆓 Free to use

## Tech Stack

- **Frontend**: Next.js, Tailwind CSS, React Hooks
- **Backend**: Python FastAPI
- **Video Processing**: yt-dlp

## Getting Started

### Prerequisites

- Node.js 14.0 or later
- Python 3.8 or later
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vieurl.git
cd vieurl
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Install backend dependencies:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Application

1. Start the frontend development server:
```bash
cd frontend
npm run dev
```

2. Start the backend server:
```bash
cd backend
uvicorn main:app --reload
```

The application will be available at [http://localhost:3000](http://localhost:3000)

## Project Structure

```
vieurl/
├── frontend/          # Next.js frontend
│   ├── pages/        # Page components
│   ├── components/   # Reusable components
│   └── styles/       # CSS styles
└── backend/          # Python FastAPI backend
    ├── main.py      # Main application file
    └── utils/       # Utility functions
```

## API Endpoints

- `POST /api/extract-info/` - Get video information
- `POST /api/download/` - Generate download link

## Environment Variables

Create a `.env.local` file in the frontend directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Next.js](https://nextjs.org/) - The React Framework
- [Tailwind CSS](https://tailwindcss.com/) - For styling
- [FastAPI](https://fastapi.tiangolo.com/) - For the backend API
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - For video extraction

## Contact

Your Name - [@yourgithub](https://www.linkedin.com/in/vishwanath-nitin-raj-33b1022b9/)
Project Link: [https://github.com/yourusername/vieurl](https://github.com/nitinrajg/vieurl) 
