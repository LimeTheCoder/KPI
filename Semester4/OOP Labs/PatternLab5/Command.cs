using System;
using System.Collections;
using System.Collections.Generic;

namespace PatternLab5
{
	abstract class Command {
		public abstract void Execute();
	}

	class AddCommand : Command {
		private Editor editor;
		private string str;

		public AddCommand(Editor e, string str_to_add) {
			editor = e;
			str = str_to_add;
		}

		public override void Execute () {
			editor.AddPeace (str);
		}
	}

	class RemoveCommand : Command {
		private Editor editor;
		private int num;

		public RemoveCommand(Editor e, int num_to_remove) {
			editor = e;
			num = num_to_remove;
		}

		public override void Execute () {
			editor.RemovePeace (num);
		}
	}

		
	// Receiver
	class Editor {
		private string curr;

		public Editor(string str) {
			curr = str;
		}

		public void AddPeace(string peace) {
			curr += peace;
		}

		public void RemovePeace(int char_num) {
			if (char_num > curr.Length)
				return;
			curr = curr.Remove (curr.Length - char_num);
		}

		public void SystemTrouble() {
			curr = "";
		}

		public void Show() {
			Console.WriteLine (curr);
		}
	}

	// Invoker
	class User {
		private Editor editor;
		private List<Command> commands;

		public User() {
			editor = new Editor ("");
			commands = new List<Command>();
		}

		public void AddStr(string str) {
			AddCommand command = new AddCommand (editor, str);
			command.Execute ();
			commands.Add (command);
		}

		public void RemoveStr(int cnt) {
			RemoveCommand command = new RemoveCommand (editor, cnt);
			command.Execute ();
			commands.Add (command);
		}

		public void Restore() {
			foreach (Command c in commands) {
				c.Execute ();
			}
		}

		public void Trouble() {
			editor.SystemTrouble ();
		}

		public void Show() {
			editor.Show ();
		}
	}
}
	
