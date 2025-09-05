''' - komentārs sākas
print() - izvada uz ekrāna argumenta vērtību
input() - atgriež no tastatūras ievadītu tekstuālo vērtību,kā argumentu var izmantot paskaidrojumu
int() - atgriež un pārveido argumentu veselā skaitli,ja pārveide nav iespējama atriež kļūdu
float() - atgriež un pārveido argumentu decimālā skaitli,ja pārveide nav iespējama atriež kļūdu
type() - atgriež argumentu datu tipu
= - piešķir
== = vienāds
+ - saskaita 2 skaitļus vai saliek 2 virknes kopā
- - atņem 2 skaitļus
* - sareizina 2 skaitļus vai ja virkni reizina ar veselu - atkārto virknes tik reizes cik liels ir skaitlis
/ - vienkāršā dalīšana(kā matemātikā)
// - dalīšana iegūstot veselo daļu
% - dalīšana iegūstot atlikumu
and - loģiskais un
or - loģiskais vai
not - loģiskais ne (pretstats)
a=>5 a==5 or a>5
True - loģiskais patiesums
False - loģiskais aplams

'''
# - vienas rindiņas komentārs

a = int(input("Ievadi a="))
b = int(input("Ievadi b="))
print(type(a))
print(type(b))
c=a*b
print(c)
