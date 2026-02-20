# 🖥️ Rdp-Control (Hybrid TCP/UDP Remote Desktop)

> **מערכת לשליטה מרחוק  ב-Python**
>
> מערכת שנועדה לשליטה בין מחשבים מרחוק.
>  המערכת משלבת תקשורת TCP לשליטה אמינה במקלדת ובעכבר, ותקשורת UDP לשידור מסך בזמן אמת (Low Latency Streaming).

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python)
![Architecture](https://img.shields.io/badge/Architecture-Hybrid%20TCP%2FUDP-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

---

## 📖 ארכיטקטורה ופרוטוקולים (Architecture)

הפרויקט בנוי בארכיטקטורת **Client-Server** חכמה המנצלת את היתרונות של שני הפרוטוקולים:

### 1. 📡 ערוץ שידור מסך
* **פרוטוקול:** UDP (User Datagram Protocol).
* **למה UDP?** שידור וידאו בזמן אמת דורש מהירות מקסימלית. ב-UDP אין אמינות שנוצרת בעזרת לחיצת היד המשולשת, מה שמאפשר להזרים פריימים (FPS) בקצב גבוה ללא השהיות מיותרות גם אם לא כל הפריימים יגיעו.

### 2. 🎮 ערוצי שליטה 
* **פרוטוקול:** TCP (Transmission Control Protocol)
* **למה TCP?** בפקודות שליטה (כמו לחיצת עכבר, הזזת עכבר, או הקלדת סיסמה) האמינות היא קריטית. TCP מבטיח שכל פקודה תגיע ליעדה בסדר הנכון ובשלמותה.

---

## 📂 מבנה הפרויקט (Project Structure)

### 🎮 Attacker (הצד השולט)
מחשב זה מציג את המסך ושולח את פקודות השליטה.
* `start_attacker.py`: סקריפט ההרצה הראשי. מפעיל את התהליכים (Threads) הדרושים.
* `app.py`: מנהל את ממשק המשתמש .
* `get_frames.py`: השרת שמאזין ומקבל את תמונות המסך (Frames).
* `send_mouse_b.py`:השרת מאזין ומקבל הקלקות עכבר
* `send_mouse_p.py`:השרת מאזין ומקבל מיקום עכבר
* `ImgTO/`: תיקייה לשמירה זמנית של פריימים שהתקבלו.

### 🎯 Client (הצד הנשלט/המטרה)
המחשב עליו מתבצעת השליטה.
* `start_server.py`: סקריפט ההרצה הראשי.
* `client.py`: מנהל את החיבור לשרת לשליחת הפריימים.
* `mini_screenshot.py`: אחראי על צילום המסך, דחיסת התמונות .
* `get_mouse_clicks.py`: סקריפט לקבלת הקלקות עכבר וביצוע.
* `get_mouse_postion.py`:  סקריפט לקבלת מיקום עכבר והזזה.
* `get_keyboard_presses.py`:  סקריפט לקבלת הקלדות מקלדת וביצוע.


