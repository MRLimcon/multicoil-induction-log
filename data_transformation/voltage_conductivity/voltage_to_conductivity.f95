module voltage_to_conductivity
  implicit none
  complex, parameter :: i_number = (0, 1)
  real, parameter :: pi = 3.14159265358979
  real, parameter :: magnetic_permeability = pi * 4 * (10**(-7))

contains

  function calculate_geometric_factor( &
        emitter_turns, &
        receiver_turns, &
        emitter_area, &
        receiver_area, &
        e_r_distance, &
        frequency) result(geometric_factor)
    implicit none

    real, intent(in) :: emitter_turns(3), receiver_turns(3), frequency(3)
    real, intent(in) :: emitter_area(3), receiver_area(3), e_r_distance(3, 3)
    integer :: i, j
    complex :: geometric_factor(3, 3)

    do i = 1, 3 ! emitter
      do j = 1, 3 ! receiver
        geometric_factor(i, j) = emitter_turns(i)*emitter_area(i)*&
              receiver_turns(j)*receiver_area(j)*(frequency(i)**2)/e_r_distance(i,j)
      end do
    end do

    geometric_factor = geometric_factor*(magnetic_permeability**2)/(4*pi)

  end function calculate_geometric_factor

  function calculate_transimpedance(voltage, current) result(transimpedance)
    implicit none
    complex, intent(in) :: voltage(3, 3), current(3)
    integer :: i, j
    complex :: transimpedance(3, 3)

    do i = 1, 3 ! emitter
      do j = 1, 3 ! receiver
        transimpedance(i, j) = voltage(i, j)/current(i)
      end do
    end do

  end function calculate_transimpedance

end module voltage_to_conductivity
