using System;
using System.Collections.Generic;

namespace PatternLab3 {

	abstract class UserPrototype {
		public string Login { get; set; }
		public string Password { get; set; }
		public string Full_Name { get; set; }
		public int Age { get; set; }
		public string City { get; set; }
		public string Font_Color { get; set; }

		public virtual UserPrototype Clone() {
			return (UserPrototype)this.MemberwiseClone();
		}
	}

	class CommonUser : UserPrototype {}

	class Admin : UserPrototype {
		public string Admin_Password { get; set; }

		public void DoAdminStuff() {
			Console.WriteLine(this.Login + " doing admin work");
		}
	}

	class UserFactory {
		private CommonUser userPrototype;
		private Admin adminPrototype;
		private static UserFactory instance;

		protected UserFactory() {
			userPrototype = new CommonUser();
			adminPrototype = new Admin();
		}

		public static UserFactory getFactory() {
			if (instance == null)
				instance = new UserFactory();
			return instance;
		}

		public CommonUser createUser() {
			return (CommonUser)userPrototype.Clone();
		}

		public Admin createAdmin() {
			return (Admin)adminPrototype.Clone();
		}
	}
}
