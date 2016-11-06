using System;

namespace PatternLab4
{
	public interface iPrimitives {
		string Operation1();
		string Operation2();
	}

	class Recipe {
		public static void Cook(iPrimitives p) {
			string task1 = "Take potato, butter, salt, sugar, species, greens\n";
			string task2 = "Clean up goods\n";
			string task3 = "Cut goods\n";
			string res = task1 + task2 + task3 + p.Operation1() + p.Operation2();
			Console.Write (res);
		}
	}

	class BoiledPotato : iPrimitives {
		public string Operation1() {
			return "Boil potato\n";
		}

		public string Operation2() {
			return "Add salt\n";
		}
	}

	class FriedPotato : iPrimitives {
		public string Operation1() {
			return "Fry potato\n";
		}

		public string Operation2() {
			return "Add species\n";
		}
	}

	class AmateurPotato : iPrimitives {
		public string Operation1() {
			return "Mixing\n";
		}

		public string Operation2() {
			return "Adding sugar\n";
		}
	}
}

