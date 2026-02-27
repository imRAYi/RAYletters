@echo off
cls
echo 🚀 Starting Rayan's Auto-Upload to RAYanime...

:: المزامنة أولاً لتجنب الـ Rejection
git pull origin RAYanime

:: الرفع
git add .
git commit -m "Auto-update from Rayan Tool"
git push origin RAYanime

echo ✨ DONE! Rayletters.life is now updating...
pause