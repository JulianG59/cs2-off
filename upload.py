cd "C:\Users\Memez\Desktop\dump\output"

git init
git branch -M main
git remote add origin https://github.com/JulianG59/cs2-off.git

git pull origin main --allow-unrelated-histories

git add .
git commit -m "Upload files"

git push origin main



git config --global user.name "JulianG59"
git config --global user.email ""


cd "C:\Users\Memez\Desktop\dump"

git config --global user.name "JulianG59"
git config --global user.email "julianossa2406@gmail.com"

git add .

git commit -m "Upload"

git branch -M main

git remote add origin https://github.com/JulianG59/cs2-off.git

git push -u origin main