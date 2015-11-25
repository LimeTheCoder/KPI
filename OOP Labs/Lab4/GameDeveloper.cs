using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPLab3 {
    [Serializable]
    class GameDeveloper : Programmer {
        public string Favorite_Game { get; set; }

        public GameDeveloper(int sal, string name, string lang, string fav_game) : base(sal, name, lang) {
            Favorite_Game = fav_game;
        }

        public override void Speak() {
            Console.WriteLine("Hello, my name is {0} and I'm game developer.", Name);
        }

        public void WorkOnGame() {
            if (Satiety > 70 && Fun > 70 && Energy > 70)
                Console.WriteLine("{0} created great part of game", Name);
            else
                Console.WriteLine("{0} created not impressive part of game", Name);

            Satiety = 0;
            Fun = 0;
            Energy = 0;
        }
    }
}
