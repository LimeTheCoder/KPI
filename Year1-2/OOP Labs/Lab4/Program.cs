using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPLab3 {
    class Program {

        static void Main(string[] args) {
            Programmer Jessy = new Programmer(1500, "Jessy", "Scala");
            Programmer Bob = new Programmer(1500, "Bob", "Java");
            Student Marty = new Student("Marty", "Calculus", true);
            GameDeveloper Garry = new GameDeveloper(2500, "Garry", "C++", "Mario");
            Programmer Danny = (Programmer)Jessy.Clone();
            
            Organization<iProgrammer> org = new Organization<iProgrammer>();
            org.AddNewMember(Jessy);
            org.AddNewMember(Bob);
            org.AddNewMember(Garry);

            Organization<iProgrammer> org2 = new Organization<iProgrammer>("Evil Corp");
            org2.AddNewMember(Bob);
            org2.AddNewMember(Garry);
            org.AddNewMember(Jessy);

            Programmer.Serialize("org.dat", org2);
            Organization<iProgrammer> org3 = (Organization<iProgrammer>)Programmer.Deserialize("org.dat");
            Console.WriteLine("Name: {0}, Count : {1}", org3.Name, org3.Count);

            Console.WriteLine("{0}", org2.CompareTo(org));

            foreach (iProgrammer programmer in org)
                programmer.CodeHard();

            org = null;

            Object[] array = new Object[500000];

            for (int i = 0; i < 500000; i++)
                array[i] = new Object();

            WeakReference reference = new WeakReference(array);
            Console.WriteLine("Is alive : " + reference.IsAlive.ToString());
            Console.WriteLine("{0}", GC.GetGeneration(Jessy.Name));
            array = null;

            GC.Collect();
            GC.WaitForPendingFinalizers();

            /*
            GC.Collect(0, GCCollectionMode.Forced);
            GC.WaitForPendingFinalizers();
            GC.Collect(1, GCCollectionMode.Forced);
            GC.WaitForPendingFinalizers();
            GC.Collect(2, GCCollectionMode.Forced);
            GC.WaitForPendingFinalizers();
            */
            //Console.WriteLine("{0}", GC.GetGeneration(Jessy.Name));
            Console.WriteLine("Is alive : " + reference.IsAlive.ToString());
            Console.WriteLine("Max gen: {0}", GC.MaxGeneration);
        }
    }
}