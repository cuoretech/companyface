## header.mako
    <div class="header row-fluid">
      <div class="logo"> <a href="index.html"><span>Cuore</span><span class="icon"></span></a> </div>
      <div class="top_right">
        <ul class="nav nav_menu">
          <li class="dropdown"> <a class="dropdown-toggle administrator" id="dLabel" role="button" data-toggle="dropdown" data-target="#" href="${request.route_url('Profile')}">
            <div class="title"><span class="name">${user.userInstance['first_name']}</span><span class="subtitle">${user.userInstance['req_title']}</span></div>
            <%doc><div class="title"><span class="name">${user.userInstance['first_name']}</span><span class="subtitle">${user.userInstance['req_title']}</span></div></%doc>
            <%doc><div class="title"><span class="name">${user.first_name}</span><span class="subtitle">${user.getTitle()}</span></div></%doc>
            % if user.getPhoto() is not None:
            <span class="icon"><img height="100" width="100" src="${request.static_url(user.getPhoto())}"></span></a>
            % else:
            <span class="icon"> IMAGE WOULD<br>GO HERE<!--<img src="">-->
            </span></a>
            <!-- End .span6 -->
            %endif
            <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">
              <li><a href="${request.route_url('Profile')}"><i class=" icon-user"></i> My Profile</a></li>
              <li><a href="${request.route_url('Registration')}"><i class=" icon-cog"></i>Settings</a></li>

<!--              <li><a href="index2.html"><i class=" icon-unlock"></i>Log Out</a></li>
              <li><a href="search.html"><i class=" icon-flag"></i>Help</a></li>-->
            </ul>
          </li>
        </ul>
      </div>
      <!-- End top-right -->
    </div>
    <!-- End header -->

