# ToDo-List
A fully functioning To-Do list using Django to manage the back-end

So far we have three views, and only one app. The Homepage view displays all of the tasks,
 the status view displays a single task and lets you edit it, 
and the newTask one lets you add a new one. Since we're using task names as IDs instead of actual IDs
 (just an experimental thingy, I wanted to see what would go wrong), we can't really create two different tasks with the same name.
The model is 'Rejectable' instead of 'Task' because the project started as the 'rejected' project suggested on a list of web app projects on Medium I found.
I changed the code but not the model, so everything is different except for var names.
I will probably change all that in the next update, but it doesn't affect the user experience at all, nor the functions.
