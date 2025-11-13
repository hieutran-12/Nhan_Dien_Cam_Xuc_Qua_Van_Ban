# 🧠 Hệ thống Phân tích Cảm xúc - BARTPho

Hệ thống phân tích cảm xúc văn bản tiếng Việt sử dụng BARTPho và Transformers.

## 📋 Tính năng

- ✅ Phân tích 7 loại cảm xúc: Yêu thương, Vui vẻ, Tức giận, Sợ hãi, Buồn bã, Ngạc nhiên, Ghê tởm
- ✅ Hiển thị độ tin cậy cho từng cảm xúc
- ✅ Giao diện đẹp mắt với biểu đồ trực quan
- ✅ Batch processing - phân tích nhiều văn bản cùng lúc
- ✅ API RESTful với validation đầy đủ

## 🏗️ Cấu trúc dự án

```
project/
├── backend/                    # Flask Backend
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── .env
│   ├── routes/
│   │   └── emotion_routes.py
│   ├── services/
│   │   └── model_service.py
│   └── utils/
│       └── validators.py
│
└── frontend/                   # React Frontend
    ├── package.json
    ├── src/
    │   ├── App.jsx
    │   ├── components/
    │   │   ├── EmotionAnalyzer/
    │   │   ├── TextInput/
    │   │   ├── AnalyzeButton/
    │   │   ├── ResultDisplay/
    │   │   ├── EmotionCard/
    │   │   └── EmotionChart/
    │   ├── services/
    │   │   └── api.js
    │   └── utils/
    │       └── emotionConfig.js
    └── tailwind.config.js
```

## 🚀 Cài đặt

### Backend (Flask)

1. **Tạo môi trường ảo:**

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

2. **Cài đặt dependencies:**

```bash
pip install -r requirements.txt
```

3. **Cấu hình environment:**

```bash
# Copy .env.example thành .env
cp .env.example .env

# Chỉnh sửa MODEL_PATH trong .env
MODEL_PATH=D:\ChuyenDoiSo\phan_tich_cam_xuc
```

4. **Chạy server:**

```bash
python app.py
```

Server sẽ chạy tại: `http://localhost:5000`

### Frontend (React)

1. **Cài đặt dependencies:**

```bash
cd frontend
npm install
```

2. **Cấu hình Tailwind CSS:**

```bash
# Tạo file tailwind.config.js
npx tailwindcss init -p
```

Nội dung `tailwind.config.js`:

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

Thêm vào `src/index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

3. **Chạy development server:**

```bash
npm start
```

Frontend sẽ chạy tại: `http://localhost:3000`

## 📡 API Endpoints

### 1. Phân tích cảm xúc đơn lẻ

```http
POST /api/analyze
Content-Type: application/json

{
  "text": "Hôm nay tôi rất vui!"
}
```

**Response:**

```json
{
  "success": true,
  "data": {
    "label": "joy",
    "confidence": 0.8532,
    "all_scores": {
      "joy": 0.8532,
      "love": 0.0654,
      "surprise": 0.0432,
      "sadness": 0.0234,
      "anger": 0.0087,
      "fear": 0.0043,
      "disgust": 0.0018
    }
  }
}
```

### 2. Phân tích nhiều văn bản

```http
POST /api/batch-analyze
Content-Type: application/json

{
  "texts": [
    "Tôi rất vui",
    "Tôi buồn quá"
  ]
}
```

### 3. Health check

```http
GET /api/health
```

## 🎯 Sử dụng

1. Khởi động Backend và Frontend
2. Truy cập `http://localhost:3000`
3. Nhập văn bản tiếng Việt cần phân tích
4. Click "Phân tích cảm xúc"
5. Xem kết quả với biểu đồ chi tiết


