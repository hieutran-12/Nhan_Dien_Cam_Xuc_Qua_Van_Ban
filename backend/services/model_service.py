import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import Dict, Tuple
from config import Config

# Map nhãn model sang key frontend 
MODEL_TO_FRONTEND = {
    "Anger": "anger",
    "Disgust": "disgust",
    "Enjoyment": "joy",
    "Fear": "fear",
    "Other": "surprise",  
    "Sadness": "sadness",
    "Surprise": "surprise"
}

class ModelService:
    """Service để quản lý model và prediction"""
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self._load_model()
    
    def _load_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path)
            self.model.eval()
            # Lấy nhãn trực tiếp từ model
            self.model_labels = [self.model.config.id2label[i] for i in range(len(self.model.config.id2label))]
            print(f"✅ Model loaded with labels: {self.model_labels}")
            print(f"✅ Label mapping: {MODEL_TO_FRONTEND}")
        except Exception as e:
            print(f"❌ Error loading model: {str(e)}")
            raise
    
    def predict(self, text: str) -> dict:
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=Config.MAX_TEXT_LENGTH
        )

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)
            top_prob, top_label = torch.max(probs, dim=1)

        # Nhãn chính xác từ model
        model_label = self.model.config.id2label[top_label.item()]
        
        # DEBUG: In ra để kiểm tra
        print(f"📊 Input text: {text[:50]}...")
        print(f"📊 Model label: {model_label}")
        print(f"📊 Confidence: {top_prob.item():.4f}")

        # Map sang key frontend
        frontend_key = MODEL_TO_FRONTEND.get(model_label, "surprise")

        # Map all_scores chính xác
        all_scores = {}
        for i, prob in enumerate(probs[0].tolist()):
            model_label_i = self.model.config.id2label[i]
            frontend_key_i = MODEL_TO_FRONTEND.get(model_label_i, "surprise")
            # Nếu có nhiều nhãn map sang cùng 1 key, lấy max
            if frontend_key_i in all_scores:
                all_scores[frontend_key_i] = max(all_scores[frontend_key_i], prob)
            else:
                all_scores[frontend_key_i] = prob
        
        # Round scores
        all_scores = {k: round(v, 4) for k, v in all_scores.items()}

        result = {
            "key": frontend_key,
            "confidence": round(top_prob.item(), 4),
            "all_scores": all_scores
        }
        
        print(f"📊 Result: {result}\n")
        
        return result

    def batch_predict(self, texts: list) -> list:
        """
        Dự đoán cho nhiều text cùng lúc
        
        Args:
            texts: List các text cần phân tích
            
        Returns:
            List các kết quả prediction
        """
        results = []
        for text in texts:
            try:
                result = self.predict(text)
                results.append(result)
            except Exception as e:
                results.append({"error": str(e)})
        
        return results