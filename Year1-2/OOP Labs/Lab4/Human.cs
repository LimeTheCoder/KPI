using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPLab3 {

    [Serializable]
    abstract class Human {
        private static int cnt;
        private int satiety;
        private int energy;
        private int fun;
        public string Name { get; set; }

        static Human() {
            cnt = 0;
            Console.WriteLine("In static constructor");
        }

        protected Human() : this(0, 0, 0) { }

        protected Human(int new_sat, int new_energ, int new_fun) {
            Satiety = new_sat;
            Energy = new_energ;
            Fun = new_fun;
            IncrementNum();
        }

        public int Satiety {
            get {
                return satiety;
            }

            set {
                if (value < 0 || value > 100)
                    throw new ArgumentOutOfRangeException("Satiety must be in range 0 - 100");
                else
                    satiety = value;
            }
        }

        public int Fun {
            get {
                return fun;
            }

            set {
                if (value < 0 || value > 100)
                    throw new ArgumentOutOfRangeException("Fun must be in range 0 - 100");
                else
                    fun = value;
            }
        }

        public int Energy {
            get {
                return energy;
            }

            set {
                if (value < 0 || value > 100)
                    throw new ArgumentOutOfRangeException("Energy must be in range 0 - 100");
                else
                    energy = value;
            }
        }

        private static void IncrementNum() {
            cnt++;
        }

        public static int HumansNum {
            get { return cnt; }
        }

        public void Eat() {
            satiety = 100;
        }

        public void Sleep() {
            energy = 100;
        }

        public void PlayHard() {
            fun = 100;
        }

        public abstract void Speak();
    }
}
