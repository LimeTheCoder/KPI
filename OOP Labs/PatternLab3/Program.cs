using System;
using System.Collections.Generic;

namespace PatternLab3 {
	class Program {
		static void Main(string[] args) {
			PrototypeTest ();
		}

		static void PrototypeTest() {
			UserFactory factory = UserFactory.getFactory();
			Admin admin = factory.createAdmin();
			admin.Login = "cool_admin";
			admin.DoAdminStuff();
		}

		static void FactoryMethodTest() {
			Jotting fresher = new FresherJotting ();
			Console.WriteLine ("\tJotting for freshers\n");
			fresher.Display ();

			Jotting magister = new MagisterJotting ();
			Console.WriteLine ("\n\n\tJotting for magisters\n");
			magister.Display ();
		}
	}
}
