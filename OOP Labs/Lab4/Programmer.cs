using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

namespace OOPLab3 {

    public interface iProgrammer {
        string Favorite_Language { get; set; }
        int Salary { get; set; }
        void CodeHard();
    }

    [Serializable]
    class Programmer : Human, iProgrammer, ICloneable, IDisposable {
        private int salary;
        public string Favorite_Language { get; set; }
        public delegate void CodeHandler(string str);
        public event CodeHandler listener;

        public Programmer() { }

        public Programmer(int sal, string name, string lang) : this(sal, name, lang, 100, 100, 100) { }

        public Programmer(int sal, string name, string lang, int satiety, int energy, int fun) : base(satiety, energy, fun) {
            Name = name;
            salary = sal;
            Favorite_Language = lang;
        }

        ~Programmer() {
            // Console.WriteLine("In finalize method");
            Console.Beep(); // hyip
        }

        public override void Speak() {
            Console.WriteLine("Hello, my name is {1} and I'm programmer. My favorite language is {0}", Favorite_Language, Name);
        }

        public int Salary {
            get {
                return salary;
            }

            set {
                if (value < 0)
                    throw new ArgumentOutOfRangeException("Salary is positive value");
                else
                    salary = value;
            }
        }

        public static void Serialize(string file, Object obj) {
            BinaryFormatter formatter = new BinaryFormatter();

            using (FileStream fs = new FileStream(file, FileMode.OpenOrCreate)) {
                formatter.Serialize(fs, obj);
                Console.WriteLine("Object serialized");
            }
        }

        public static Object Deserialize(string file) {
            BinaryFormatter formatter = new BinaryFormatter();
            Object newProgrammer;
            using (FileStream fs = new FileStream(file, FileMode.OpenOrCreate))
            {
                newProgrammer = formatter.Deserialize(fs);

                Console.WriteLine("Object deserialized");
            }

            return newProgrammer;
        }

        public void CodeHard() {

            if (Satiety > 70 && Fun > 70 && Energy > 70)
                Console.WriteLine("{0} is writing a beautifful code", Name);
            else
                Console.WriteLine("{0} is writing a terrible code", Name);

            Satiety = 0;
            Fun = 0;
            Energy = 0;
        }

        public object Clone() {
            return this.MemberwiseClone();
        }

        public void Dispose() {
            // release unmanaged resources
            Console.WriteLine("In Dispose method!");
            GC.SuppressFinalize(this);
        }
    }
}
