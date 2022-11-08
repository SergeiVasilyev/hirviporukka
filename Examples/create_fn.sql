-- Function to get a member from jasen table by jasen id

-- Create a function and set arguments 
CREATE FUNCTION public.get_member(
	id integer)

-- Define type of result set -> jasen table's structure
RETURNS SETOF public.jasen

-- Set language to standart SQL 
LANGUAGE SQL
AS $$ -- Begin 
SELECT * FROM public.jasen WHERE jasen_id = id;
$$; -- End
	