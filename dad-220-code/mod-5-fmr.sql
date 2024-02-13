create table fmr ( vehicleid bigint, state varchar(50), repair varchar(50), reason varchar(50), year int, make varchar(20), bodytype varchar(80) );

describe fmr;

load data infile '/home/codio/workspace/FleetMaintenanceRecords.csv' into table fmr fields terminated by ',' lines terminated by '\n' ignore 1 lines;


select repair, count(*) as numOfReplacements from fmr where repair like '%replacement%' group by repair;

 


select repair, count(*) as numOfReplacementsSW from fmr where repair lik
e '%replacement%' and state IN ('AZ', 'NM', 'TX', 'OK') group by repair;

 

select repair, count(*) as numOfReplacementsSE from fmr where repair like '%replacement%' and state IN ('AR', 'LA', 'MS', 'AL', 'GA', 'FL', 'KY', 'TN',
 'SC', 'NC', 'VA', 'WV', 'DE', 'MD') group by repair;

 
select repair, count(*) as numOfReplacementsNE from fmr where repair lik
e '%replacement%' and state IN ('PA', 'NJ', 'NY', 'CT', 'RI', 'MA', 'VT', 'NH', 'ME') group by repair;

 
 
select repair, count(*) as numOfReplacementsMW from fmr where repair lik
e '%replacement%' and state IN ('ND', 'SD', 'KS', 'NE', 'MN', 'WI', 'IA', 'MO',
 'MI', 'IN', 'IL', 'OH') group by repair;

 

select repair, count(*) as numOfReplacementsWest from fmr where repair l
ike '%replacement%' and state IN ('WA', 'ID', 'MT', 'OR', 'WY', 'CO', 'UT', 'NV', 'CA') group by repair;

 

select repair, count(*) as numOfReplacementsRustCorros from fmr where repair like '%replacement%' and reason in ('Rust', 'Corrosion') group by repair;
