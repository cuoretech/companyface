#**************************************
# Current Database Info
#**************************************

#	To Access...
#	from database_config 	import db_config
#	from py2neo 			import neo4j
#		graph_db = neo4j.GraphDatabaseService(db_config['uri'])

db_config   			= {}
#db_config['address']	= "http://162.212.130.189"
db_config['address']	= "http://127.0.0.1"
db_config['port']		= "7474"
db_config['ending']		= "db/data"
db_config['uri']		= db_config['address'] 		+ ":" \
							+ db_config['port']		+ "/" \
							+ db_config['ending']	+ "/"
db_config['username'] 	= "your_username_here"
db_config['password'] 	= "your_password_here"

#Moar constants

#Relationship Constants
REL_HASEVENT 		= "has_event"
REL_HASTASK  		= "has_task"
REL_HASSUBTASK		= "has_subtask"
REL_HASDEADLINE 	= "has_deadline"
REL_HASCALENDAR 	= "has_calendar"
REL_HASSUBCALENDAR	= "has_subcalendar"
REL_HASOWNER		= "has_owner"
REL_HASGROUP		= "has_group"
REL_HASGENTASK		= "has_gentask"
REL_HASTASK			= "has_task"
REL_HASFILE			= "has_file"
REL_HASPROJECT		= "has_project"
REL_HASPOST			= "has_post"
REL_ASSIGNEDTO		= "assigned_to"
REL_CREATEDBY		= "created_by"
REL_INVITED			= "invited"
REL_HASCOMMENT      = "has_comment"
REL_HASWORKSPACE    = "has_workspace"
REL_HASDEP          = "has_dept"
REL_HASTITLE        = "has_title"
REL_HASUSER         = "has_user"
REL_ISMEMBER        = "is_member"
REL_HASBLOG         = "has_blog"
REL_UNASSIGNED      = "is_unassigned"
REL_UNCONFIRMED     = "is_unconfirmed"

#Label Constants
LBL_COMPANY     = "Company"
LBL_DEPARTMENT  = "Department"
LBL_TITLES      = "Titles"
LBL_USER		= "User"

LBL_CAL			= "Calendar"
LBL_EVENT		= "Event"
LBL_TASK		= "Task"
LBL_SUBTASK		= "SubTask"
LBL_DEADLINE	= "Deadline"
LBL_GROUP		= "Group"
LBL_WORKSPACE	= "Workspace"
LBL_PROJECT		= "Project"
LBL_FILE		= "File"
LBL_BLOG		= "Blog"
LBL_POST		= "Post"
LBL_COMMENT     = "Comment"


#Index Constants (to be replaced by Label Constants at a later time)
IND_COMP        = "Company"
IND_DEP         = "Departments"
IND_TITLE       = "Titles"
IND_USER        = "Users"
IND_UNASSIGNED  = "Unassigned"
IND_UNCONFIRMED = "Unconfirmed"

IND_CAL         = "Calendars"
IND_EVENT       = "Events"
IND_TASK        = "Tasks"
IND_SUBTASK     = "Subtasks"
IND_WORKSPACE   = "Workspaces"
IND_PROJECT     = "Projects"
IND_FILE        = "Files"
IND_BLOG        = "Blogs"
IND_POST        = "Posts"
IND_COMMENT     = "Comments"


