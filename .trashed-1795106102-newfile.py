import random
import time

# قائمة الأذكار العشوائية
azkar_list = [
    "لا حَوْلَ وَلا قُوَّةَ إِلا بِاللَّهِ (كنز من كنوز الجنة)",
    "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ ، سُبْحَانَ اللَّهِ الْعَظِيمِ (ثقيلتان في الميزان)",
    "أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ الَّذِي لا إِلَهَ إِلا هُوَ الْحَيُّ الْقَيُّومُ وَأَتُوبُ إِلَيْهِ",
    "اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ عَلَى نَبِيِّنَا مُحَمَّدٍ"
]

def tasbeeh_counter():
    print("═" * 40)
    print("       📿 مُسبحة الأذكار الإلكترونية 📿       ")
    print("═" * 40)
    print("1 - سبحان الله")
    print("2 - الحمد لله")
    print("3 - الله أكبر")
    print("4 - عرض ذكر عشوائي")
    print("5 - خروج من البرنامج")
    print("═" * 40)
    
    choice = input("اختر رقم العملية اللي حابب تبدأها يا محمد: ")
    
    if choice == '5':
        print("\nفي أمان الله يا محمد، لا تنسنا من صالح دعائك! 👋")
        return
        
    if choice == '4':
        print("\n✨ ذكر اليوم:")
        print(f"» {random.choice(azkar_list)} «")
        time.sleep(2)
        tasbeeh_counter() # العودة للقائمة الرئيسية
        return

    # تحديد الكلمة بناءً على اختيارك
    if choice == '1':
        target_mention = "سبحان الله"
    elif choice == '2':
        target_mention = "الحمد لله"
    elif choice == '3':
        target_mention = "الله أكبر"
    else:
        print("اختيار غير صحيح، جرب تاني يا بطل.")
        tasbeeh_counter()
        return

    count = 0
    print(f"\nبدأنا التعداد لـ ({target_mention}).")
    print("اضغط Enter بعد كل تسبيحة... (اكتب 'خروج' للعودة للقائمة)")
    
    while count < 33:
        user_input = input(f"[{count + 1}/33] {target_mention} ... ")
        if user_input.strip() == "خروج":
            break
        count += 1
    
    if count == 33:
        print("\n🎉 أحسنت يا محمد! ختمت الـ 33 تسبيحة كاملة.")
        print("قال النبي ﷺ: (غُفرت خطاياه وإن كانت مثل زبد البحر). تقبل الله منك.\n")
    
    time.sleep(2)
    tasbeeh_counter() # ارجع للقائمة تاني

# تشغيل التطبيق الإسلامي
if __name__ == "__main__":
    tasbeeh_counter()
