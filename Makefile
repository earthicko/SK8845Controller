NAME		= hid_to_i2c_relay
SRV			= hidi2crelay.service

CXX			= c++
CXXFLAGS	= -Wall -Wextra -Werror

SRCS		= main.cpp
OBJS		= $(SRCS:.cpp=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $@ $(LDFLAGS)

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re:
	make fclean
	make all

$(SRV):
	./create_service.sh $(NAME) $(SRV)

install: all $(SRV)
	cp ./$(SRV) /lib/systemd/system/$(SRV)
	chmod 644 /lib/systemd/system/$(SRV)
	systemctl daemon-reload
	systemctl enable $(SRV)
	systemctl start $(SRV)
	hostnamectl set-hostname bthidhub

.PHONY: all clean fclean re
