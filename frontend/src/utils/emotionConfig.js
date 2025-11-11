const EMOTION_CONFIG = {
  love: {
    emoji: "💖",
    labelVi: "Yêu thương",
    color: "#E91E63",
  },
  joy: {
    emoji: "😊",
    labelVi: "Vui vẻ",
    color: "#FF9800",
  },
  anger: {
    emoji: "😠",
    labelVi: "Tức giận",
    color: "#F44336",
  },
  fear: {
    emoji: "😨",
    labelVi: "Sợ hãi",
    color: "#9C27B0",
  },
  sadness: {
    emoji: "😢",
    labelVi: "Buồn bã",
    color: "#2196F3",
  },
  surprise: {
    emoji: "😲",
    labelVi: "Ngạc nhiên",
    color: "#FF5722",
  },
  disgust: {
    emoji: "🤢",
    labelVi: "Ghê tởm",
    color: "#4CAF50",
  },
};

/**
 * Lấy cấu hình cho emotion
 * @param {string} emotion - Tên emotion
 * @returns {Object} - Cấu hình emotion
 */
export const getEmotionConfig = (emotion) => {
  return EMOTION_CONFIG[emotion] || EMOTION_CONFIG.joy;
};

export default EMOTION_CONFIG;
