#include "DebugPrint.h"
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <stdio.h>
#include <sys/epoll.h>
#include <sys/ioctl.h>
#include <unistd.h>

#define MAX_EVENTS 2
#define BUF_SIZE 1024
#define I2C_ADDR 0x55

const char *path_i2c_bus = "/dev/i2c-1";
const char *path_hid_kbd = "/dev/hidraw0";
const char *path_hid_mse = "/dev/hidraw1";

int main()
{
	int fd_i2c, fd_kbd, fd_mse, fd_ep;
	char buffer[BUF_SIZE];
	struct epoll_event event;

	if ((fd_i2c = open(path_i2c_bus, O_WRONLY)) < 0)
	{
		printf("Failed to open the i2c bus");
		return (1);
	}

	if (ioctl(fd_i2c, I2C_SLAVE, I2C_ADDR) < 0)
	{
		printf("Failed to acquire bus access and/or talk to slave.\n");
		return (1);
	}

	fd_kbd = open(path_hid_kbd, O_RDONLY | O_NONBLOCK);
	fd_mse = open(path_hid_mse, O_RDONLY | O_NONBLOCK);
	DEBUG_PRINTF("opened fd at %d %d\n", fd_kbd, fd_mse);

	fd_ep = epoll_create(1);
	DEBUG_PRINTF("epoll created at %d\n", fd_ep);

	event.events = EPOLLIN;
	event.data.fd = fd_kbd;
	epoll_ctl(fd_ep, EPOLL_CTL_ADD, fd_kbd, &event);
	event.data.fd = fd_mse;
	epoll_ctl(fd_ep, EPOLL_CTL_ADD, fd_mse, &event);

	while (true)
	{
		struct epoll_event events[MAX_EVENTS];
		int num_events = epoll_wait(fd_ep, events, MAX_EVENTS, -1);

		for (int i = 0; i < num_events; i++)
		{
			int ready_fd = events[i].data.fd;
			ssize_t count = read(ready_fd, buffer, sizeof(buffer));
			if (count > 0)
			{
				DEBUG_PRINTF("read %d: ", count);
				for (ssize_t j = 0; j < count; j++)
					DEBUG_PRINTF("%d ", buffer[j]);
				DEBUG_PRINTF("\n");

				if (write(fd_i2c, buffer, count) != count)
					printf("Failed to write to the i2c bus.\n");
			}
		}
	}

	close(fd_kbd);
	close(fd_mse);
	close(fd_ep);

	return (0);
}
