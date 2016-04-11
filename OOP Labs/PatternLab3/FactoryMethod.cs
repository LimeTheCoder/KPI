using System;
using System.Collections;
using System.Collections.Generic;

namespace PatternLab3
{
	abstract class JottingUnit {
		public string information;

		public JottingUnit(string inf) {
			information = inf;
		}

		public string GetUnitInformation() {
			return information;
		}

		public void PrintUnit() {
			Console.WriteLine (information);
		}
	}

	class UniversityMap : JottingUnit {
		public UniversityMap() : base("University map part") { }
	}

	class NumberInformation : JottingUnit {
		public NumberInformation() : base("Number information part") { }
	}

	class Syllabus : JottingUnit {
		public Syllabus () : base("Syllabus") { }
	}

	class UniversityRules : JottingUnit {
		public UniversityRules() : base("University rules part") { }
	}

	class MagisterProgram : JottingUnit {
		public MagisterProgram() : base("Magister program page") { }
	}

	class ResearchTips : JottingUnit {
		public ResearchTips() : base("Research tips page") { }
	}

	abstract class Jotting {
		protected List<JottingUnit> units;

		public Jotting() {
			units = new List<JottingUnit> ();
			this.GenerateUnits ();
		}

		protected abstract void GenerateUnits ();

		public void Display() {
			foreach(JottingUnit unit in units) {
				unit.PrintUnit ();
			}
		}
	}

	class FresherJotting : Jotting {
		protected override void GenerateUnits() {
			units.Add (new UniversityMap ());
			units.Add (new NumberInformation ());
			units.Add (new Syllabus ());
			units.Add (new UniversityRules ());
		}
	}

	class MagisterJotting : Jotting {
		protected override void GenerateUnits() {
			units.Add (new MagisterProgram ());
			units.Add (new ResearchTips ());
		}
	}
}

