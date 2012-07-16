create keyspace test;
use test;


create column family Test with comparator=UTF8Type
and column_metadata=[

{column_name: idd, validation_class: },


{column_name: noidd, validation_class: },

];




