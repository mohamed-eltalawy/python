import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score
from imblearn.over_sampling import SMOTE

# تحميل البيانات
df = pd.read_csv("arabic_names.csv")

# معالجة القيم الفارغة في العمودين الأساسيين
df = df.dropna(subset=["names", "sex"])

# ترميز الجنس (F → 0, M → 1)
label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["sex"])  # ← ده العمود اللي هنستخدمه مع النموذج

# الميزات والهدف
X = df["names"].fillna("")
y = df["label"]

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تحويل الأسماء إلى شعاع رقمي باستخدام TF-IDF
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 5))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# معالجة عدم التوازن باستخدام SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_vec, y_train)

# عرض التوزيع بعد SMOTE
print("✅ Resampled class distribution:")
print(pd.Series(y_train_resampled).value_counts())

# تدريب النموذج
model = XGBClassifier(
    random_state=42,
    eval_metric='logloss',
    use_label_encoder=False,
    max_depth=4,
    learning_rate=0.1,
    n_estimators=100,
    subsample=0.8,
    colsample_bytree=0.8
)

model.fit(X_train_resampled, y_train_resampled)

# التنبؤ على بيانات الاختبار
y_pred = model.predict(X_test_vec)

# التقييم
print("🔍 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📋 Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))




import joblib

# حفظ الموديل
joblib.dump(model, 'xgb_gender_model_v3.pkl')

# حفظ الـ TfidfVectorizer
joblib.dump(vectorizer, 'tfidf_vectorizer_v3.pkl')

# حفظ الـ LabelEncoder
joblib.dump(label_encoder, 'label__encoder_v3.pkl')

print("✅ تم حفظ الموديل و الأدوات بنجاح.")
