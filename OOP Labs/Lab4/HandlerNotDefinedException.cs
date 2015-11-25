using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOPLab3 {
    class HandlerExceptionArgs {
        public string msg { get; set; }
        public Exception exception { get; set; }

        public HandlerExceptionArgs(string message, Exception except) {
            msg = (string)message.Clone();
            exception = except;
        }
    }

    class HandlerNotDefinedException : Exception {
        public HandlerNotDefinedException() { }
        public HandlerNotDefinedException(string msg) : base(msg) { }
        public HandlerNotDefinedException(string msg, Exception innerException) : base(msg, innerException) { }
        public HandlerNotDefinedException(HandlerExceptionArgs args) : base(args.msg, args.exception) { }
    }
}
