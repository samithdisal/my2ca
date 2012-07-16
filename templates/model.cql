create keyspace ${keyspace};
use ${keyspace};

% for ccf in t:
${cf(ccf)}
% endfor

<%def name="cf(cf)">
create column family ${cf.name} with comparator=UTF8Type
and column_metadata=[
% for c in cf.cols:
${col(c)}
% endfor
];
</%def>

<%def name="col(col)">
% if col.indexed:
{column_name: ${col.name}, validation_class: ${col.custype}, index_type: KEYS,},
% else:
{column_name: ${col.name}, validation_class: ${col.custype}},
% endif
</%def>