BEGIN {
        printf "{ \"body\": \"# [![ShiftLeft](https://res-4.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_120,w_120,f_auto,b_white,q_auto:eco/v1504497223/fildsndtwbaa2e7gw6qb.png)](https://shiftleft.io) NG-SAST Analysis Compliance Failure\\n\\n" ;
        RS = "\n";
        FS = " ";
        APPL = "nothing";
}

/\[INFO\] Using app/ {
        APPL=$4;
}

/New matching finding / {
  printf "* [ID %s](https://shiftleft.io/findingDetail/%s/%s) %s", $6, APPL, $6, $7 ;
  FS = ":";
  $0 = $0;
}

/New matching finding/ {
  printf "%s: %s\\n", $2, $3 ;
  FS = " ";
  $0 = $0;
}

END {
  print "\" }"
}
