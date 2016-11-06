using System;
using System.Collections;
using System.Collections.Generic;

namespace PatternLab4
{

	abstract class ConverterStrategy
	{
		protected abstract string ConvertMark(int mark);

		public List<string> Convert (List<int> marks) {
			List<string> converted_marks = new List<string>();
			marks.ForEach (mark => converted_marks.Add(ConvertMark(mark)) );
			return converted_marks;
		}
	}

	class ExamStrategy : ConverterStrategy {

		protected override string ConvertMark(int mark) {
			if (mark >= 95) return "A";
			if (mark >= 85) return "B";
			if (mark >= 75) return "C";
			if (mark >= 65) return "D";
			if (mark >= 60) return "E";
			if (mark >= 36) return "Fx";
			return "F";
		}
	}

	class CreditStrategy : ConverterStrategy {
		protected override string ConvertMark(int mark) {
			if(mark >= 60) return "Passed";
			else return "Not passed";
		}
	}

	class StrategyContext {
		private ConverterStrategy converter;

		public StrategyContext(ConverterStrategy strategy) {
			converter = strategy;
		}

		public List<string> Convert(List<int> marks) {
			return converter.Convert (marks);
		}
	}
}

