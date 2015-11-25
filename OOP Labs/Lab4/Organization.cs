using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPLab3 {
    [Serializable]
    class Organization<T> : IEnumerable, IComparable {
        private List<T> org;

        public string Name { get; set; }

        public Organization() : this("MyCompany") {
        }

        public Organization(string name) {
            Name = name;
            org = new List<T>();
        }

        public int Count {
            get {
                return org.Count;
            }
        }

        public T this[int i] {
            get {
                try {
                    return org[i];
                }
                catch(Exception e) {
                    Console.WriteLine("{0}", e.Message);
                    throw e;
                }
            }

            set {
                try {
                    org[i] = value;
                }
                catch(Exception e) {
                    Console.WriteLine("{0}", e.Message);
                    throw e;
                }
            }
        }

        public void AddNewMember(T member) {
            org.Add(member);
        }

        public bool RemoveMember(T member) {
            if (org.Contains(member)) {
                org.Remove(member);
                return true;
            }
            else
                return false;
        }

        IEnumerator IEnumerable.GetEnumerator() {
            return org.GetEnumerator();
        }

        public int CompareTo(object obj) {
            Organization<T> another = obj as Organization<T>;
            if (another == null)
                throw new Exception("Not comparable objects");
            if (Count < another.Count) return -1;
            if (Count > another.Count) return 1;

            return 0;
        }
    }
}
