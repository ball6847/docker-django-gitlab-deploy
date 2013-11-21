#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

#define BIN "/usr/bin/git"


char std::string get_working_path()
{
    char temp [255];

    if (getcwd(temp, 255) == 0)
    {
        return std::string(temp);
    }

    int error = errno;

    switch (error)
    {
        // EINVAL can't happen - size argument > 0

        // PATH_MAX includes the terminating nul, 
        // so ERANGE should not be returned

        case EACCES:
            throw std::runtime_error("Access denied");

        case ENOMEM:
            // I'm not sure whether this can happen or not 
            throw std::runtime_error("Insufficient storage");

        default: {
            std::ostringstream str;
            str << "Unrecognised error" << error;
            throw std::runtime_error(str.str());
        }
    }
}

class GitWrapper
{
    public:
        char repo;
        char bin[] = "/usr/bin/git";
        int pull(void);
        GitWrapper(char path);
}

GitWrapper::GitWrapper(char path)
{
    if ( ! chdir(path))
    {
        throw std::runtime_error("Cannot chdir to specified working directory");
    }
    
    repo = path
}

int GitWrapper::pull(void)
{
    FILE *process_p = popen("git", "pull", "origin", "master");
    
    if ( ! git_pull_p)
    {
        return -1;
    }
    
    char output[1024];
    char *buffer_p = fgets(output, sizeof(output), process_p);
    pclose(process_p);
    
    return 1;
}

int main(int argc, char** argv)
{
    char user[32]  = argb[1];
    char repo[255] = argv[2];
    
    GitWrapper git(argv[2]);
    return git.pull();
}
