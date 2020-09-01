using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace peepoopoosad
{
    class Program
    {
        static Random nummer = new Random(); // den här gör så att man kan slumpa fram en int gömd i variabeln "nummer" 
        static int riktig = nummer.Next(1, 11); // den här slumpar en int mellan 1-10
        static int hp = 0; // sätter bara ett värde på hp som är 0 innan man väljer hur många försök man ska ha
        static bool playing = true;  // flyttade playing hit för att det ska vara mer prydligt
        static void Main() // hela spelet
        {
            while (playing)
            {
                //bool playing = true;
                bool penis = false;
                while (!penis)
                {
                    // frågar hur många liv du vill spela med och lagrar det i "hp"
                    Console.WriteLine("hur många liv vill du spela med?");
                    string fag = Console.ReadLine();
                    penis = int.TryParse(fag, out hp);
                    if (!penis)
                    {
                        //kollar så att du inte använder bokstäver när du svarar hur många liv du vill ha.
                        Console.WriteLine("etablera kommunism i samhället. det betyder att du inte ska använda bokstäver");
                        Console.ReadKey(true);
                        Console.Clear();
                    }

                }
                //dialog 
                riktig = nummer.Next(1, 11);
                Console.WriteLine("nu ska jag ge dig en utmaning");
                Console.WriteLine("jag tänker på ett tal mellan 1 och 10. du ska gissa vilket det är. om du har fel så får du gissa om.");
                Console.WriteLine("låter det kul?");
                Console.WriteLine("nej? fan va synd då");
                Console.WriteLine("klicka för att gå vidare");
                Console.ReadKey(true);
                Console.Clear();
                Console.WriteLine("nu tänker jag på ett tal");
                Console.WriteLine("gissa vilket");
                while (hp > 0)
                {
                    //medans hu har hp som är över 0 så säger den att du har ("mängd hp" försök kvar)
                    Console.WriteLine(hp + " försök kvar");
                    hp--;
                    generator(); // kallar på funktionen "generator"

                }
                köraom(); // om ditt hp är 0 så kallar den på köraom funktionen 
                Console.ReadKey(true);

            }

        }
        // nu börjar vi med generatorn och koden bakom spelet
        static void generator()
        {
            int kuk = 0;
            bool bokstavskoll = false;
            while (!bokstavskoll)
            //ser till så att du inte gissar med bokstäver
            {
                string gissning2 = Console.ReadLine();
                bokstavskoll = int.TryParse(gissning2, out kuk);
                if (!bokstavskoll)
                {
                    Console.WriteLine("nej inga jävla bokstäver. gissa med siffror");
                    Console.ReadKey(true);
                    Console.Clear();
                    Console.WriteLine("gissa vilket");
                }

            }
            // svarar du inte med bokstäver så säger den om ditt svar var för litet eller för mycket eller rätt.
            if (kuk < riktig)
            {
                Console.WriteLine("nej nästan. lite mer dock. ett till försök");
                Console.ReadKey(true);
                Console.Clear();
                if (hp > 0)
                {
                    Console.WriteLine("gissa igen");
                }
                else if (hp == 0)
                {
                    Console.WriteLine("BYE BYE JOJO!");
                }

            }
            else if (kuk == riktig) // har man rätt så gratulerar den dig och sätter ditt hp på 0 så att du inte har extra liv kvar efter att du har vunnit
            {
                Console.WriteLine("hahahahahahaahhahahahahahah ja!");
                Console.Beep(69, 1000);
                Console.ReadKey(true);
                hp = 0;
            }
            else if (kuk > riktig)
            {
                Console.WriteLine("nej mindre. försök igen");
                Console.ReadKey(true);
                Console.Clear();
                Console.WriteLine("gissa igen");
                //om ditt hp nåt 0 så säger den "BYE BYE JOJO!"
                if (hp == 0)
                {
                    Console.WriteLine("BYE BYE JOJO!");
                }
            }
        }
        static void köraom()
        // frågar om du vill spela igen och ger svaret ett värde som är sant eller falskt beroende på vad du svarat. ger "playing" ett sant eller falskt värde som ser till att du kan eller inte kan spela igen.
        {
            Console.WriteLine("vill du spela igen");
            string svar = Console.ReadLine();
            if (svar == "ja")
            {
                playing = true;
            }
            else if (svar == "nej")
            {
                Console.WriteLine("jaha tjarå");
                playing = false;
            }
            else
            {
                Console.WriteLine("svara med ja eller nej");
                köraom();
            }
        }

    }
}
