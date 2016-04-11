using System;
using System.Collections;
using System.Collections.Generic;

namespace PatternLab4
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			// StrategyTest ();
			PatternMethodTest ();
		}

		public static void StrategyTest() {
			ConverterStrategy strategy = new ExamStrategy ();
			StrategyContext context = new StrategyContext (strategy);
			List<int> marks = new List<int> () { 87, 64, 59, 98, 77, 65, 32 };
			List<string> res = context.Convert (marks);
			res.ForEach (value => Console.WriteLine (value));
		}

		public static void PatternMethodTest() {
			iPrimitives dish = new BoiledPotato ();
			Console.WriteLine ("\t\tBoiled potato\n");
			Recipe.Cook (dish);
			dish = new FriedPotato ();
			Console.WriteLine ("\t\tFried potato\n");
			Recipe.Cook (dish);
			dish = new AmateurPotato ();
			Console.WriteLine ("\t\tAmateur potato\n");
			Recipe.Cook (dish);
		}
	}
}
