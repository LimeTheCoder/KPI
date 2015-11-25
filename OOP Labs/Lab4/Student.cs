using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPLab3 {
    
    public interface iStudent {
        string Favorite_Subject { get; set; }
        int Grant { get; }
        void LearnHard();
    }

    [Serializable]
    class Student : Human, iStudent, ICloneable {
        public string Favorite_Subject { get; set; }
        private static int grants;
        private bool has_grant;

        static Student() {
            grants = 1000;
        }

        public Student(string name, string subj, bool grant) : this(name, subj, grant, 100, 100, 100) { }

        public Student(string name, string subj, bool grant, int satiety, int energy, int fun) : base(satiety, energy, fun) {
            Name = name;
            Favorite_Subject = subj;
            has_grant = grant;
        }

        public int Grant {
            get {
                if (has_grant)
                    return grants;
                else
                    return 0;
            }
        }

        public override void Speak() {
            Console.WriteLine("Hello, my name is {0} and I'm student. My favorite subject is {1}", Name, Favorite_Subject);
        }

        public void LearnHard() {
            if (Satiety > 70 && Fun > 70 && Energy > 70)
                Console.WriteLine("{0} well learned new material", Name);
            else
                Console.WriteLine("{0} poorly learned new materiale", Name);

            Satiety = 0;
            Fun = 0;
            Energy = 0;
        }

        public object Clone() {
            return this.MemberwiseClone();
        }
    }
}
