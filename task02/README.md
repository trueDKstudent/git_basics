## Task2

Code examples 02ex01 and 02ex02 are added to folder task02.
Changes that were applied to code 02ex02 are commited on
branch **dev**.

# task for 02ex01:

Script require next values: `initial sum, percent, fixed period, set period`.
If initial sum is not specified then only three next arguments should be entered.

Example with specified initial sum:

```
[vit@vm task02]$ python3 02ex01-deposits.py 23 5 1 2
1-year yield:  24.15,  in percentage +5%
Monthly yield:  23.09,  in percentage +0%
5-year yield:  29.35,  in percentage +28%
10-year yield:  37.46,  in percentage +63%


total yield:  25.36,  in percentage +10%
```
Here fixed period is specified in years. As a result script calculated
new sum after one year, one month, five years and 10 years. Sum that was
calculaed with custom **set perido**, which is 2 years in this case, is
displayed below.

Example with unknown initial sum:

```
[vit@vm task02]$ python3 02ex01-deposits.py 5 0.0833 2
1-year yield:  in percentage +80%
Monthly yield:  in percentage +5%
5-year yield:  in percentage +1770%
10-year yield:  in percentage +34873%


total yield:  in percentage +223%
```

Here **set period** is set to one month which is equal to 1/12 of one year.
Also if initial sum is not specified script shows only percents.

# task for 02ex02:

The abbility to choose drinks was added to script. Now user can also enter **beer,**
**vine, vodka** or **rom** to get one or more of the listed drinks.

Example:

```
[vit@vm task02]$ python3 02ex02-vikings.py 
Welcome to the Vikings restaurant.
What would you like to eat?
> egg without beer
Disgusting. Who eats egg without beer?
We highly recommend egg and double portion of sausage and double portion of spam, and sausage, rom and rom and double portion of rom, and beer, and beer...
	Tip: Next time call "02ex02-vikings.py num" to set number of dishes.
[vit@vm task02]$ 
```
