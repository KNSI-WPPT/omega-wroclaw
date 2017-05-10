# omega-wroclaw
## Utils
- database backup 
  `mysqldump.exe -h <instance address> -u <login> -p <remote db> --single-transaction > dump.sql`
- upload to local db
  `mysql.exe -u <local user name> -p <local db> < dump.sql`
