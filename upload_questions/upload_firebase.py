#!/usr/bin/env python3
"""
رفع أسئلة لعبة حروف مع ريان على Firebase Firestore
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
قبل التشغيل:
1. نزّل ملف Service Account من Firebase Console:
   Project Settings → Service accounts → Generate new private key
2. احفظ الملف باسم serviceAccountKey.json في نفس مجلد هذا السكريبت
3. شغّل: pip install firebase-admin
4. ثم: python3 upload_firebase.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import json
import os

try:
    import firebase_admin
    from firebase_admin import credentials, firestore
except ImportError:
    print("❌ firebase-admin غير مثبت. شغّل: pip install firebase-admin")
    exit(1)

# ─── تحميل الأسئلة ───
with open("questions.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

# ─── اتصال Firebase ───
SERVICE_KEY = "serviceAccountKey.json"
if not os.path.exists(SERVICE_KEY):
    print(f"❌ ملف {SERVICE_KEY} غير موجود.")
    print("   نزّله من: Firebase Console → Project Settings → Service accounts")
    exit(1)

cred = credentials.Certificate(SERVICE_KEY)
firebase_admin.initialize_app(cred)
db = firestore.client()

# ─── رفع الأسئلة ───
print("جاري رفع الأسئلة على Firestore...")
collection = db.collection("questions")

for letter, questions in QUESTIONS.items():
    doc_ref = collection.document(letter)
    doc_ref.set({"questions": questions})
    print(f"  ✅ {letter}: {len(questions)} سؤال")

print(f"\n🎉 تم رفع {sum(len(v) for v in QUESTIONS.values())} سؤال لـ {len(QUESTIONS)} حرف بنجاح!")
