FortiOS - Filtering results
Filtering results
A Configuration query and a Monitor query will return all results. To refine the number of results, the following options are available:

filtering

sorting

paging

formatting

Filtering, paging, and formatting were added to Monitor API in FortiOS 6.4.2 and are almost equivalent to filtering, paging, and formatting for Configuration API. The one exception is that Configuration API does a deep search for filter keywords, while Monitor API uses the syntax “parent.child.value” to specify the keyword in nested objects.

Sorting was added to both Configuration and Monitor API in FortiOS 6.4.2.

 

Filtering
To filter results, include the “filter” parameter in the request URL parameter:

filter=[key][operator][pattern]
 

The following filter operators are supported:

Operator

Case sensitive

Description

==

Yes

Pattern must be identical to the value.

=*

No

Pattern must be identical to the value.

!=

Yes

Pattern does not match the value.

!*

No

Pattern does not match the value.

=@

No

Pattern found within value.

!@

No

Pattern not found within value.

<=

n/a

Value must be less than or equal to pattern.

<

n/a

Value must be less than pattern.

>=

n/a

Value must be greater than or equal to pattern.

>

n/a

Value must be greater than pattern.

 

Examples:

To display firewall policies with the schedule “always”, use:

/api/v2/cmdb/firewall/policy?filter=schedule==always
To display available-interfaces that do not have the name “wan1”, use:

/api/v2/monitor/system/available-interfaces?filter=name!=wan1
 

To create a complex query, filters can be combined as follows:

Combination

How to use it

Logical OR

Separate each key-operator-value within the same filter using commas ‘,’. This only works for same key and same operator. 

Example: filter=key1op1value1,key1op1value2

Logical AND

Separate each set of filters using ampersands ‘&’. This can work for different sets of key, operator, value.

Example: filter=key1op1value1&filter=key2op2value2

Combining AND and OR

You can AND different sets of OR filters using an ampersand '&'.

Example: filter=key1op1value1,key1op1value2&filter=key3op3value3

 

Examples:

To display firewall policies using the “always” schedule OR the “once” schedule, use:

/api/v2/cmdb/firewall/policy?filter=schedule==always,schedule==once
To display firewall policies with a schedule of “always” AND an action of “accept”, use:

/api/v2/cmdb/firewall/policy?filter=schedule==always&filter=action==accept
To display firewall policies with a schedule of “always” AND an action of either “accept” or “deny”, use:

/api/v2/cmdb/firewall/policy?filter=schedule==always&filter=action==accept,action==deny
To display available certificates with a name of “@Fortinet” AND an issuer.CN of “@Fortinet”, use:

/api/v2/monitor/system/available-certificates?filter=name=@Fortinet&filter=issuer.CN=@Fortinet
 

 
Escaped characters
The “.” and “\” characters need to be escaped if they are part of a filter pattern.

Character

Escaped Value

.

\.

\

\\

 

Sorting
To sort results, include the “sort” parameter in the request URL parameter:

sort=[key]
There is an optional second field that specifies the order (asc: ascending, dsc: descending) and defaults to asc.

Examples:

To sort by name in ascending order, use:

sort=name
To sort by version in descending order, use:

sort=version,dsc
Multiple keywords can be specified with the first one having the highest priority:

sort=version,dsc&sort=name,asc
Results will be sorted in the order entered. In the example above, results will be sorted in descending order of the “version” field; entries with the same version will be sorted in alphabetic order of the “name” field.

To sort available certificates descending by “q_ref” with entries having an identical “q_ref” sorted ascending by “name”, use:

/api/v2/monitor/system/available-certificates?&sort=q_ref,dsc&sort=name,asc
 

Paging
Paging limits the number of entries returned by including one or both of the “start” and “count” parameters:

start=[starting entry index]&count=[Maximum number of entries to return]
For example, to display 50 of 100 results starting with the 10th result, use:

start=10,count=50
An error will occur when:

start > number of entries

count > number of entries

All results will be returned when:

start + count > number of entries

start or count is negative

start and count are set to 0

 

Formatting
To return only specific fields in the results, include the “format” parameter in the request URL parameter:

format=[property1]|[property2]|...
For example, to display only the policyid and srcintf fields, use:

format=policyid|srcintf
For Monitor API, the format parameter also accepts objects specified using the syntax “parent.child.value”. For example, to display only “name”, “issuer.C” and “q_ref” fields in the results, use:

format=name|issuer.C|q_ref
When an invalid field name is specified, all results will be returned.

 

Combining parameters
When filtering, sorting, paging, and formatting parameters are included in one query, they will be applied in the following order:

Filtering

Sorting

Paging

Formatting

The order in which parameters are included in the request does not matter.

Examples

Query 1:

/api/v2/monitor/system/available-interfaces?format=name&filter=name=@wan
The base query returns all available interfaces. Next,

the filter parameter retains only items that contain “wan” (case insensitive) in the “name” field.
the format parameter returns only the “name” field .
Query 2:

/api/v2/cmdb/firewall/address?format=name|type|sub-type&sort=name,dsc&filter=name=@ADDR,type==ipmask&filter=name=@r&start=4&count=3
The base query returns all firewall addresses. Next,

the filter parameter retains only items that meet one or both of:
the “name” field contains “@ADDR” (case insensitive)
the “type” field is exactly “ipmask”
the sort parameter sorts the results in descending order by the “name” field
the start and count parameters retain only three (3) items starting with the item at index 4
the format parameter returns only the “name”, “type”, and “sub-type” fields.
Query 3:

/api/v2/monitor/firewall/proxy-policy?format=policyid|last_used|hit_count|uuid&sort=uuid,dsc&filter=hit_count<1&start=2&count=3
The base query returns all firewall proxy policies. Next,

the filter parameter retains only items that have a value greater than 1 in the “hit_count” field
the sort parameter sorts the results in descending order by the “uuid” field.
the start and count parameters retain only three (3) items starting with the item at index 2
the format parameter returns only the “policyid”, “last_used”, “hit_count”, and “uuid” fields.
 

Note:

This order in which filtering parameters are applied is not followed for individual API that had the start and count parameters prior to FortiOS 6.4.2. For these API, paging will occur before filtering and sorting. The same is true for filters, in the paging will occur before filtering.

Example

The base query returns 9,8,7,6,5,4,3,2,1.

The query parameters are: sort=number,asc&start=3&count=3

API

Is paging new in 6.4.2?

Results

Configuration

yes

4, 5, 6

Configuration

no

4, 5, 6

Monitor

yes

4, 5, 6

Monitor

no

6, 7, 8

This page was updated as of FortiOS 6.4.2 when filtering, paging, and formatting were added to Monitor API and sorting was added to Configuration and Monitor API. The previous version of this page is available at Filtering results 6.4.1 and earlier.