@echo off
:: تنظيف الشاشة
cls
echo 🚀 Starting Rayan's Auto-Upload...

:: تنفيذ أوامر الـ Git
git add .
git commit -m "Auto-update from Rayan Tool"
git push origin RAYanime

echo ✨ DONE! Rayletters.life is now updating...
pause