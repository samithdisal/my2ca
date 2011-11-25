create keyspace ${keyspace};
use ${keyspace};

<%def name="cf(cf)">

create column family ${cf.name} with comparator=UTF8Type
and column_metadata=[
% for c in cf.cols:
${col(c)}
% endfor
];

</%def>

<%def name="col(col)>
{column_name: ${col.name}, validation_class: ${col.custype}},
</%def>