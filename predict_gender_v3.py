##  cd d:/BA/iw/gender-classifier/


import pandas as pd
import joblib

# تحميل الأدوات المحفوظة
model = joblib.load("xgb_gender_model_v3.pkl")
vectorizer = joblib.load("tfidf_vectorizer_v3.pkl")
label_encoder = joblib.load("label__encoder_v3.pkl")

# تحميل الملف الجديد اللي فيه عمود name
df_new = pd.read_excel("names_to_predict.xlsx")

# تجهيز عمود gender مبدئيًا
df_new["gender"] = "Unknown"

# التعامل مع الصفوف اللي فيها أسماء فعلًا
mask = df_new["name"].notna()

# تحويل النصوص للشكل الرقمي المطلوب للموديل
X_new_vec = vectorizer.transform(df_new.loc[mask, "name"])

# التنبؤ بالجنس
preds = model.predict(X_new_vec)

# عكس الترميز الرقمي إلى F / M
df_new.loc[mask, "gender"] = label_encoder.inverse_transform(preds)

# حفظ الملف الجديد
df_new.to_excel("predicted_names_with_unknown.xlsx", index=False)
print("✅ الملف اتعمل بنجاح باسم predicted_names_with_unknown.xlsx ويحتوي على Unknown للأسماء الفاضية.")
