using System;
using System.Collections;
using System.Collections.Generic;

namespace PatternLab5
{
	class ProducingCenter {
		private List<Artist> artists = new List<Artist>();
		private Dictionary<string, Client> clients = new Dictionary<string, Client>();

		public void RegisterClient(Client c) {
			clients.Add (c.Name, c);
		}

		public void RegisterArtist(Artist a) {
			artists.Add (a);
		}

		public void RequestProgram(string client, int age, int show_pop, string date) {
			List<String> program = new List<String> ();
			foreach (Artist artist in artists) {
				if (artist.Age < age) {
					if (artist.SignContract (show_pop, date))
						program.Add (artist.Name);
				}
			}
			if (clients.ContainsKey (client))
				clients [client].ConcertProgram = program;
		}
	}

	class Artist {
		public string Name { get; set;}
		public int Age { get; set; }
		public int SingerPopularity{ get; set; }
		public string NextConcertDate { get; set; }

		public Artist(string name, int age, int pop) {
			Age = age;
			Name = name;
			SingerPopularity = pop;
			NextConcertDate = "";
		}

		public bool SignContract(int show_popularity, string date) {
			if (NextConcertDate == date || 
				(SingerPopularity - show_popularity) > 10)
				return false;
			NextConcertDate  = date;
			return true;
		}
	}

	class Client {
		private ProducingCenter producingCenter;
		public List<String> ConcertProgram { get; set; }
		public string Name { get; set; }

		public Client(ProducingCenter m, string name) {
			producingCenter = m;
			Name = name;
			ConcertProgram = new List<string> ();
		}

		public void RequestProgram(int age, int show_popularity,
		                           string concert_date) {

			if (producingCenter != null)
				producingCenter.RequestProgram(Name, age,
				                               show_popularity, 
				                               concert_date); 
		}

		public void DisplayConcertProgram() {
			foreach (string artist_name in ConcertProgram) {
				Console.WriteLine (artist_name);
			}
		}
	}

}

