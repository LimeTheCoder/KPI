using System;

namespace PatternLab5
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			CommandTest ();
		}

		public static void CommandTest() {
			User user = new User ();
			user.AddStr ("Hello");
			user.AddStr (" world!mda");
			user.RemoveStr (3);
			//user.Show ();
			user.Trouble ();
			user.Restore ();
			user.Show ();
		}

		public static void MediatorTest() {
			ProducingCenter center = new ProducingCenter ();
			Artist a = new Artist ("Jack Lover", 23, 74);
			center.RegisterArtist (a);
			a = new Artist ("Jinny James", 34, 65);
			center.RegisterArtist (a);
			a = new Artist ("Patty Kerry", 27, 85);
			center.RegisterArtist (a);
			a = new Artist ("Rob Jonhes",42, 58);
			center.RegisterArtist (a);
			a = new Artist ("Ice Cube", 29, 77);
			center.RegisterArtist (a);

			Client c = new Client (center, "Lesley Williams");
			center.RegisterClient (c);
			c.RequestProgram (40, 70, "2016-04-25");
			c.DisplayConcertProgram ();
		}
	}
}
