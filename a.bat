for /r "C:\Users\Rafael\Desktop\folhas-20230912T163503Z-001\folhas" /d %%d in (*) do (
    cd "%%d"
    magick mogrify -resize 512x512 -format png *.heic
    cd ..
)