from gi.repository import Notify
Notify.init ("hello world")
Hello=Notify.Notification.new ("Hello world",
                                                            "This is an example notification."
                                                            , "dialog-information")
Hello.show ()                                                            
