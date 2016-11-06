using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace OOP_Lab1
{
    class Matrix {
        protected double[,] data;

        public int GetSize(int dimension = 0) {
            if (dimension == 0 || dimension == 1)
                return data.GetLength(dimension);
            else
                throw new Exception("[GetSize method] Wrong dimension");
        }

        public Matrix() { }

        public Matrix(int m, int n) : this(m, n, null) { }

        public Matrix(double[,] arr) : this(arr.GetLength(0), arr.GetLength(1), arr) { }

        private Matrix(int m, int n, double[,] arr) {
            CheckSize(m, n);

            if (arr != null)
                data = (double[,])arr.Clone();
            else
                data = new double[m, n];
        }

        public void Display() {
            for (int i = 0; i < GetSize(0); i++) {
                for (int j = 0; j < GetSize(1); j++)
                    Console.Write("{0} ", data[i, j]);
                Console.WriteLine();
            }
        }

        public double this[int m, int n] {
            get {
                try { return data[m, n]; }
                catch(IndexOutOfRangeException e) {
                    Console.WriteLine("{0}", e.Source);
                    Console.WriteLine("[{1}] {0}", e.Message, DateTime.Now);
                    return 0;
                }
                catch {
                    throw new NullReferenceException(String.Format("[{0}][Appel to the matrix by index][Matrix is not initialized][Error]", DateTime.Now));
                }
            }
            set {
                try { data[m, n] = value; }
                catch (IndexOutOfRangeException e) {
                    Console.WriteLine("Value '{0}' was not assigned to index.", value);
                    Console.WriteLine("[{1}] {0}", e.Message, DateTime.Now);
                }
                catch {
                    throw new NullReferenceException(String.Format("[{0}][Appel to the matrix by index][Matrix is not initialized][Error]", DateTime.Now));
                }
            }
        }

        public static Matrix operator + (Matrix a, Matrix b) {
            return new Matrix(a.AddTo(b.data));
        }

        public static Matrix operator -(Matrix a, Matrix b) {
            return new Matrix(b.SubstractFrom(a.data));
        }

        public static Matrix operator *(Matrix a, Matrix b) {
            return new Matrix(a.MultiplyTo(b.data));
        }

        public static Matrix operator *(Matrix a, double b) {
            return new Matrix(a.MultiplyTo(b));
        }

        public void ReadFromFile(StreamReader sr) {
            int[] size = new int[2];

            string str = null;
            if (sr == null || (str = sr.ReadLine()) == null) {
                Logger.Record("Read matrix from file", false, "File is empty");
                throw new IOException("File is empty");
            }

            int j = 0;

            try {
                foreach (string col in str.Trim().Split(' ')) {
                    size[j] = int.Parse(col);
                    j++;
                }
            }

            catch {
                Logger.Record("Read matrix from file", false, "Cannot read size from file");
                throw new Exception("Error reading size of matrix from file");
            }

            CheckSize(size[0], size[1]);
            data = new double[size[0], size[1]];

            try {
                for (int i = 0; i < size[0]; i++) {
                    j = 0;
                    foreach (string col in sr.ReadLine().Trim().Split(' ')) {
                        data[i, j] = double.Parse(col);
                        j++;
                    }
                }
            }

            catch {
                Logger.Record("Read matrix from file", false, String.Format("Matrix({0}x{1}) was not readed", size[0], size[1]));
                throw new Exception(String.Format("[Reading matrix][Error][Matrix({0}x{1}) was not readed]", size[0], size[1]));
            }

            Logger.Record("Reading matrix from file", true);
        }

        protected virtual void CheckSize(int m, int n) {
            if (m < 1 || n < 1) {
                Logger.Record("Reading from file/Check size", false, "Incorrect initial size");
                throw new IndexOutOfRangeException("Incorrect height or width of matrix");
            }
        }

        protected double[,] AddTo(double[,] a) {
            if (a.GetLength(0) != this.GetSize(0) || a.GetLength(1) != this.GetSize(1)) {
                Logger.Record("Sum operation", false, "Nonconformant size of matrix");
                throw new Exception(String.Format("[Operator '+'] Error. " +
                    "Nonconformant arguments(op1 is {0}x{1}, op2 is {2}x{3})", a.GetLength(0), a.GetLength(1), this.GetSize(0), this.GetSize(1)));
            }

            double[,] res = new double[a.GetLength(0), a.GetLength(1)];

            for (int i = 0; i < a.GetLength(0); i++) {
                for (int j = 0; j < a.GetLength(1); j++)
                    res[i, j] = a[i, j] + this[i, j];
            }

            Logger.Record("Add two matrix", true);
            return res;
        }

        protected double[,] SubstractFrom(double[,] a) {
            if (a.GetLength(0) != this.GetSize(0) || a.GetLength(1) != this.GetSize(1)) {
                Logger.Record("Substart operation", false, "Nonconformant size of matrix");
                throw new Exception(String.Format("[Operator '-'] Error. " +
                    "Nonconformant arguments(op1 is {0}x{1}, op2 is {2}x{3})", a.GetLength(0), a.GetLength(1), this.GetSize(0), this.GetSize(1)));
            }

            double[,] res = new double[a.GetLength(0), a.GetLength(1)];

            for (int i = 0; i < a.GetLength(0); i++) {
                for (int j = 0; j < a.GetLength(1); j++)
                    res[i, j] = a[i, j] - this[i, j];
            }
            Logger.Record("Substart operation", true);
            return res;
        }

        protected double[,] MultiplyTo(double [,] b) {
            if (this.GetSize(1) != b.GetLength(0)) {
                Logger.Record("Multiply operation", false, "Nonconformant size of matrix");
                throw new Exception(String.Format("[Operator '*'] Error. " +
                    "Nonconformant arguments(op1 is {0}x{1}, op2 is {2}x{3})", this.GetSize(0), this.GetSize(1), b.GetLength(0), b.GetLength(1)));
            }

            double [,] res = new double[this.GetSize(0), b.GetLength(1)];

            for (int i = 0; i < this.GetSize(0); i++) {
                for (int j = 0; j < b.GetLength(1); j++) {
                    for (int k = 0; k < b.GetLength(0); k++)
                        res[i, j] += this[i, k] * b[k, j];
                }
            }
            Logger.Record("Multiply operation", true);
            return res;
        }

        protected double[,] MultiplyTo(double num) {
            double[,] res = new double[this.GetSize(0), this.GetSize(1)];

            for(int i = 0; i < this.GetSize(0); i++) {
                for (int j = 0; j < this.GetSize(1); j++)
                    res[i, j] = this[i, j] * num;
            }
            Logger.Record("Multiply at number operation", true);
            return res;
        }

        public double EuclidNorm() {
            double res = 0;

            for (int i = 0; i < this.GetSize(0); i++)
                for (int j = 0; j < this.GetSize(1); j++)
                    res += this[i, j] * this[i, j];

            return Math.Sqrt(res);
        }

        public void Write(StreamWriter wr) {
            if (wr == null)
                throw new Exception("[Write method] Bad StreamWriter");

            for(int i = 0; i < GetSize(0); i++) {
                for (int j = 0; j < GetSize(1); j++)
                    wr.Write("{0} ", this[i, j]);
                wr.WriteLine();
            }
            Logger.Record("Writing matrix into file", true);
        }

    }

    class SquareMatrix : Matrix { 
        public SquareMatrix(int size) : base(size, size) {}
        private SquareMatrix(double[,] arr) : base(arr) {
            if(arr.GetLength(0) != arr.GetLength(1)) {
                data = null;
                throw new Exception("[SquareMatrix class] Array is not square. Use Matrix class constructor");
            }
        }

        public SquareMatrix() { }

        public static SquareMatrix operator +(SquareMatrix a, SquareMatrix b) {
            return new SquareMatrix(a.AddTo(b.data));
        }

        public static SquareMatrix operator -(SquareMatrix a, SquareMatrix b) {
            return new SquareMatrix(b.SubstractFrom(a.data));
        }

        public static SquareMatrix operator *(SquareMatrix a, SquareMatrix b) {
            return new SquareMatrix(a.MultiplyTo(b.data));
        }

        public static SquareMatrix operator *(SquareMatrix a, double b) {
            return new SquareMatrix(a.MultiplyTo(b));
        }

        public double RowNorm() {
            double max = 0;

            for (int i = 0; i < this.GetSize(); i++) {
                double tmp = 0;

                for (int j = 0; j < this.GetSize(); j++)
                    tmp += Math.Abs(this[i, j]);

                if (tmp > max)
                    max = tmp;
            }

            return max;
        }

        public double ColNorm() {
            double max = 0;

            for (int i = 0; i < this.GetSize(); i++) {
                double tmp = 0;

                for (int j = 0; j < this.GetSize(); j++)
                    tmp += Math.Abs(this[j, i]);

                if (tmp > max)
                    max = tmp;
            }

            return max;
        }

        protected override void CheckSize(int m, int n) {
            base.CheckSize(m, n);
            if (m != n)
                throw new IndexOutOfRangeException("[Read] Matrix is not square, use matrix class instead of SquareMatrix");
        }
    }

    class Vector : Matrix {
        private Vector(double[,] arr) : base(arr){
            if (arr.GetLength(0) != 1 && arr.GetLength(1) != 1) {
                data = null;
                throw new Exception("[Vector class] Array is not vector. Use Matrix class constructor");
            }
        }

        public Vector() { }

        public static Vector operator +(Vector a, Vector b) {
            return new Vector(a.AddTo(b.data));
        }

        public static Vector operator -(Vector a, Vector b) {
            return new Vector(b.SubstractFrom(a.data));
        }

        public static Matrix operator *(Vector a, Vector b) {
            return new Matrix(a.MultiplyTo(b.data));
        }

        public static Vector operator *(Vector a, double b) {
            return new Vector(a.MultiplyTo(b));
        }

        protected override void CheckSize(int m, int n) {
            base.CheckSize(m, n);
            if (m != 1 && n != 1)
                throw new IndexOutOfRangeException("[Read] Matrix is not vector, use matrix class instead of vector");
        }

        public double SumNorm() {
            double res = 0;
            for (int i = 0; i < GetSize(0); i++) {
                for (int j = 0; j < GetSize(1); j++)
                    res += Math.Abs(this[i, j]);
            }

            return res;
        }

        public double MaxNorm() {
            double max = 0;
            for (int i = 0; i < GetSize(0); i++) {
                for(int j = 0; j < GetSize(1); j++)
                    if (max < Math.Abs(this[i, j])) max = Math.Abs(this[i, j]);
            }
            return max;
        }

    }

    static class Logger {
        static private StreamWriter writer;

        static public void Record(string action, bool state, string comment = null) {
            string str = String.Format("[{0}][{1}]", DateTime.Now, action);
            if (comment != null)
                str += "[" + comment + "]";
            str += (state ? "[OK]" : "[Error]");
            writer.WriteLine(str);
        }

        static public void init() {
            writer = new StreamWriter(@"D:\log.txt");
        }

        static public void close() {
            writer.Close();
        }
    }

    class Program {
        static void Main(string[] args) {
            Logger.init();
            StreamWriter wr = new StreamWriter(@"D:\out.txt");
            try {
                StreamReader sr = new StreamReader(@"D:\input.txt");
                SquareMatrix A = new SquareMatrix();
                Matrix B = new Matrix();
                Matrix C = new Matrix();
                Vector X = new Vector();
                Vector Y = new Vector();
                A.ReadFromFile(sr);
                //A.Display();
                B.ReadFromFile(sr);
                //B.Display();
                C.ReadFromFile(sr);
                //C.Display();
                X.ReadFromFile(sr);
                //X.Display();
                Y.ReadFromFile(sr);
                //Y.Display();
                Matrix res = (A * B + C) * (X - Y);
                res.Display();
                res.Write(wr);
                Console.WriteLine("Euclid norm: {0}", res.EuclidNorm());
            }
            catch(Exception e) {
                Console.WriteLine("{0}", e.Message);
            }
            Logger.close();
            wr.Close();
        }
    }
}
